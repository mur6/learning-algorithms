/// # 問題
/// 2020/07/14
/// https://atcoder.jp/contests/abc170/tasks/abc170_a
///
/// # 提出
/// https://atcoder.jp/contests/abc170/submissions/17902370

fn main() {
    let s = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        s.trim_end().to_owned() // 改行コードが末尾にくっついてくるので削る
    };
    // let numbers: Vec<i32> = s.split(' ').map(|s| s.trim())     // (2)
    //           .filter(|s| !s.is_empty())        // (3)
    //           .map(|s| s.parse().unwrap())      // (4)
    //           .collect();
    let numbers: Vec<i32> = s.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    let index = numbers.iter().position(|&n| n == 0).unwrap();
    println!("{}", index + 1);
}
