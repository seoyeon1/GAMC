// goorm ide에서 언어로 jS 선택 > 입력 받는 방법 
// run by Node.js

// readline 모듈 : process.stdin 같은 스트림으로부터 데이터를 읽을 때 필요한 인터페이스 제공
const readline = require('readline');


// [방법1]
const rl = readline.createInterface({ // readline.Interface 클래스 인스턴스 생성
    input: process.stdin, 
    output: process.stdout 
}); 

// line 이벤트 : input 스트림이 /n 나 /r을 받을 때 발생(사용자가 입력 후 엔터 누를 때)

// 한 줄 입력 : question(출력메시지, 콜백함수)
rl.question('문자를 입력 : ', function (line) {
    console.log(line); // 입력받은 값 확인
    rl.close();
});

let count = 0;

// 여러 줄 입력
rl.on('line', function (line) { 
    // 입력을 원하는 만큼 받으려면, 특정 조건에 rl.close();가 실행되도록 추가
    // if(line == "quit") rl.close(); // quit이 아닌 이상 계속 입력 받음
    console.log(line); 
    count++;
    if(count === 5){ // 5줄 입력받고 종료
        rl.close();
    }
});
// close 이벤트 : close 이벤트가 발생 > Interface 인스턴스도 종료

rl.on('close', function () { // 실행 : rl.close()호출 / input스트림이 end이벤트를 받을 때
    process.exit(); 
});


// [방법2] JS의 비동기 처리 패턴

// const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) { // 입력값을 line으로 한줄씩 읽어와
		console.log('Hello Goorm! Your input is', line);
		rl.close(); // process.exit()를 호출 > 프로세스 종료
        // close()가 없다면, 엔터를 쳐도 여러 줄 입력 가능. ctrl + c로 프로세스 종료
	}
	
	process.exit();
})();
