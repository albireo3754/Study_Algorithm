mod fetcher;
mod problem;
use crate::fetcher::{Problem, CodeDefinition};
use std::fs;
use std::io::Write;
use std::path::Path;
use regex::Regex;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    
    if (args.len() > 1) {
        let id = args[1].parse::<u32>().unwrap();
        let problem = fetcher::get_problem(id).unwrap_or_else(|| {
        panic!(
            "Error: failed to get problem #{} \
             (The problem may be paid-only or may not be exist).",
            id
        )});
        let code = problem
        .code_definition
        .iter()
        .find(|&d| d.value == "rust".to_string())
        .unwrap();
        deal_problem(&problem, &code, true);
        return;
    } else {
        panic!("no args!");
    };
}


fn parse_extra_use(code: &str) -> String {
    let mut extra_use_line = String::new();
    // a linked-list problem
    if code.contains("pub struct ListNode") {
        extra_use_line.push_str("\nuse crate::util::linked_list::{ListNode, to_list};")
    }
    if code.contains("pub struct TreeNode") {
        extra_use_line.push_str("\nuse crate::util::tree::{TreeNode, to_tree};")
    }
    if code.contains("pub struct Point") {
        extra_use_line.push_str("\nuse crate::util::point::Point;")
    }
    extra_use_line
}

fn parse_problem_link(problem: &Problem) -> String {
    format!("https://leetcode.com/problems/{}/", problem.title_slug)
}

fn parse_discuss_link(problem: &Problem) -> String {
    format!(
        "https://leetcode.com/problems/{}/discuss/?currentPage=1&orderBy=most_votes&query=",
        problem.title_slug
    )
}

fn insert_return_in_code(return_type: &str, code: &str) -> String {
    let re = Regex::new(r"\{[ \n]+}").unwrap();
    match return_type {
        "ListNode" => re
            .replace(&code, "{\n        Some(Box::new(ListNode::new(0)))\n    }")
            .to_string(),
        "ListNode[]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "TreeNode" => re
            .replace(
                &code,
                "{\n        Some(Rc::new(RefCell::new(TreeNode::new(0))))\n    }",
            )
            .to_string(),
        "boolean" => re.replace(&code, "{\n        false\n    }").to_string(),
        "character" => re.replace(&code, "{\n        '0'\n    }").to_string(),
        "character[][]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "double" => re.replace(&code, "{\n        0f64\n    }").to_string(),
        "double[]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "int[]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "integer" => re.replace(&code, "{\n        0\n    }").to_string(),
        "integer[]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "integer[][]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<String>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<TreeNode>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<boolean>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<double>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<integer>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<list<integer>>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<list<string>>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "list<string>" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "null" => code.to_string(),
        "string" => re
            .replace(&code, "{\n        String::new()\n    }")
            .to_string(),
        "string[]" => re.replace(&code, "{\n        vec![]\n    }").to_string(),
        "void" => code.to_string(),
        "NestedInteger" => code.to_string(),
        "Node" => code.to_string(),
        _ => code.to_string(),
    }
}

fn build_desc(content: &str) -> String {
    // TODO: fix this shit
    content
        .replace("<strong>", "")
        .replace("</strong>", "")
        .replace("<em>", "")
        .replace("</em>", "")
        .replace("</p>", "")
        .replace("<p>", "")
        .replace("<b>", "")
        .replace("</b>", "")
        .replace("<pre>", "")
        .replace("</pre>", "")
        .replace("<ul>", "")
        .replace("</ul>", "")
        .replace("<li>", "")
        .replace("</li>", "")
        .replace("<code>", "")
        .replace("</code>", "")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("<sub>", "")
        .replace("</sub>", "")
        .replace("</sup>", "")
        .replace("<sup>", "^")
        .replace("&nbsp;", " ")
        .replace("&gt;", ">")
        .replace("&lt;", "<")
        .replace("&quot;", "\"")
        .replace("&minus;", "-")
        .replace("&#39;", "'")
        .replace("\n\n", "\n")
        .replace("\n", "\n * ")
}


fn deal_problem(problem: &Problem, code: &CodeDefinition, write_mod_file: bool) {
    let file_name = format!(
        "p{:04}_{}",
        problem.question_id,
        problem.title_slug.replace("-", "_")
    );
    let file_path = Path::new("./src/problem").join(format!("{}.rs", file_name));
    if file_path.exists() {
        panic!("problem already initialized");
    }

    let template = fs::read_to_string("./template.rs").unwrap();
    let source = template
        .replace("__PROBLEM_TITLE__", &problem.title)
        .replace("__PROBLEM_DESC__", &build_desc(&problem.content))
        .replace(
            "__PROBLEM_DEFAULT_CODE__",
            &insert_return_in_code(&problem.return_type, &code.default_code),
        )
        .replace("__PROBLEM_ID__", &format!("{}", problem.question_id))
        .replace("__EXTRA_USE__", &parse_extra_use(&code.default_code))
        .replace("__PROBLEM_LINK__", &parse_problem_link(problem))
        .replace("__DISCUSS_LINK__", &parse_discuss_link(problem));

    let mut file = fs::OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open(&file_path)
        .unwrap();

    file.write_all(source.as_bytes()).unwrap();
    drop(file);
    
    if write_mod_file {
        let mut lib_file = fs::OpenOptions::new()
            .write(true)
            .append(true)
            .open("./src/problem/mod.rs")
            .unwrap();
        writeln!(lib_file, "mod {};", file_name);
    }
}
