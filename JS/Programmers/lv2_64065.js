function solution(s) {
  const sets = s.match(/\{[0-9\,]+\}/g);
  const elems = new Map();
  for (let i of sets) {
    const i_ = i.slice(1, i.length - 1).split(',');
    for (let elem of i_) {
      if (elems.get(elem)) elems.set(elem, elems.get(elem) + 1);
      else elems.set(elem, 1);
    }
  }
  return [...elems].sort((a, b) => b[1] - a[1]).map((a) => Number(a[0]));
}

// if i use JSON.parser and } => ], this code will be simplify
