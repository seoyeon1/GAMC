// 1주차 1번 다시풀기 (JS)- testcase 10 실패

// Run by Node.js
const readline = require('readline');
let data = [];
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		data.push(line);
		// console.log(data);
		// rl.close();
	}
	console.log(solution(data));
	process.exit();
})();

function solution(arr){
	// let n = data[0];
	let bridges = data[1].split(' ');
	// console.log(bridges);
	
	let res = bridges.reduce((a,b)=> a*(+b), 1);
	return res;
}