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
    let k = [
        '\u{305F}', '\u{035C}', '\u{035C}', '\u{034F}',
        '\u{0318}', '\u{0323}'];
    let s: String = k.iter().collect();
    // let a: i32 = 3;
    // dbg!(a);
    // let b = (1..=10).collect::<Vec<i32>>();
    // dbg!(b);
    print!("{}", s);
}
