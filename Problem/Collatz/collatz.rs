use std::env;

fn collatz(n: u64) -> Vec<u64> {
    assert!(n > 0);
    let mut vec = Vec::new();
    let mut n = n;
    while n != 1 {
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
        vec.push(n);
    }
    vec
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = args.get(1).unwrap();
    let n: u64 =input.parse().unwrap();
    println!("{:?}", collatz(n));
}
