/// # 問題
/// 2020/07/28
/// https://atcoder.jp/contests/abc146/tasks/abc146_c
///
/// # 提出
/// https://atcoder.jp/contests/abc161/submissions/18074812
use std::cmp;

fn read() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s.trim_end().to_owned()
}

fn to_number_vector(s: &str) -> Vec<i64> {
    let numbers = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
    numbers
}

fn main() {
    println!("Hello, world!");
}
