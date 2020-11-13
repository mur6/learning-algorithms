/// # 問題
/// 2020/07/17
/// https://atcoder.jp/contests/abc161/tasks/abc161_c
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
    let s = read();
    if let &[n, k] = to_number_vector(&s).as_slice() {
        let t = n / k;
        let a1 = (n - k * t).abs();
        let a2 = (n - k * (t + 1)).abs();
        println!("{}", cmp::min(a1, a2));
    }
}
