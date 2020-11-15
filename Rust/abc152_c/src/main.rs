/// # 問題
/// 2020/07/22
/// https://atcoder.jp/contests/abc152/tasks/abc152_c
///
/// # 提出
/// https://atcoder.jp/contests/abc152/submissions/18076262
use std::cmp;
use std::i64;

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
    let n: usize = read().parse().unwrap();
    let p_list = to_number_vector(&read());
    let mut minimums = Vec::with_capacity(n);
    let mut prev = i64::MAX;
    for &p in &p_list {
        let m = cmp::min(prev, p);
        minimums.push(m);
        prev = m;
    }
    let answer_list: Vec<_> = p_list.iter().zip(minimums.iter()).filter(|(&p, &m)| p == m).collect();
    println!("{}", answer_list.len());
}
