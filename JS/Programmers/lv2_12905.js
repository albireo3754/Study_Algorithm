function solution(board)
{
//  0 is row x and 1 is col y
    let sizes = [[], []]
    for (let x = 0; x < board.length; x++) {
        sizes[0].push(board[x].reduce((acc, cur) => (acc + cur)));
    }

    for (let y = 0; y < board[0].length; y++) {
        let count = 0;
        for (let x = 0; x < board.length; x++) {
            count += board[x][y];
        }
        sizes[1].push(count)
    }
    let lenMax = Math.min(sizes[0].length, sizes[1].length);
    let canMake = [0, 0]
    while (lenMax > 0) {
        let xCnt = lenMax;
        let yCnt = lenMax;
        if (canMake[0] === 0) {            
            for (let x = 0; x < sizes[0].length; x++) {

                if (lenMax <= sizes[0][x]) {
                    xCnt -= 1;
                } else xCnt = lenMax;
                if (xCnt === 0) {
                    canMake[0] = lenMax;
                    break;
                }
            }
        }
        if (canMake[1] === 0) {
            for (let y = 0; y < sizes[1].length; y++) {

                if (lenMax <= sizes[1][y]) {
                    yCnt -= 1;
                } else yCnt = lenMax;
                if (yCnt === 0) {
                    canMake[1] = lenMax;
                    break;
                }
            }
        }
        if (canMake[0] && canMake[1]) {
            return Math.min(canMake[0], canMake[1]) ** 2; 
        }
        lenMax -= 1;
    }
    return 0
}
