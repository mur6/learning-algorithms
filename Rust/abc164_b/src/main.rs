/// # 問題
/// 2020/07/16
/// https://atcoder.jp/contests/abc164/tasks/abc164_b
///
/// # 提出
/// https://atcoder.jp/contests/abc164/submissions/18074132

fn read() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s.trim_end().to_owned()
}

fn main() {
    let s = read();
    let numbers: Vec<i32> = s.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    //println!("{:?}", numbers);
    if let &[a_point, a_offence, b_point, b_offence] = numbers.as_slice() {
         let j = (b_point as f64 / a_offence as f64).ceil();
         let k = (a_point as f64 / b_offence as f64).ceil();
        let answer = if j <= k {"Yes"} else {"No"};
        println!("{}", answer);
    }
}
