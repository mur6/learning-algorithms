use std::env;

fn collatz(n: u64) -> Vec<u64> {
    assert!(n > 0);
    let mut vec = Vec::new();
    let mut n = n;
    loop {
        vec.push(n);
        if n == 1 {
            break;
        }
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
    }
    vec
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = args.get(1).unwrap();
    let n:u64 = input.parse().unwrap();
    let answers: Vec<String> = collatz(n).into_iter().map(|i| i.to_string()).collect();
    let answer = answers.join(" ");
    println!("{}", answer);
}
