/// # 問題
/// 2020/07/13
/// https://atcoder.jp/contests/abc173/tasks/abc173_a
///
/// # 提出
/// https://atcoder.jp/contests/abc173/submissions/17901985

fn main() {
    let s = {
        let mut s = String::new(); // バッファを確保
        // 一行読む。失敗を無視
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().to_owned() // 改行コードが末尾にくっついてくるので削る
    };
    let input:i32 = s.parse().unwrap();
    let ceiled = (input as f64 / 1000.0).ceil() as i32;
    let answer:i32 = ceiled * 1000 - input;
    println!("{}", answer);
}
