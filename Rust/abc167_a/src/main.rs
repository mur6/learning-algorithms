/// # 問題
/// 2020/07/15
/// https://atcoder.jp/contests/abc167/tasks/abc167_a
///
/// # 提出
/// https://atcoder.jp/contests/abc167/submissions/17903694

fn read() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s.trim_end().to_owned()
}

fn main() {
    let s = read();
    let t = read();
    let (first, _) = t.split_at(t.len() - 1);
    let answer = if s.as_str() == first { "Yes" } else { "No" };
    println!("{}", answer);
}
