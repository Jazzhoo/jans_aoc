use std::{fs, io::Read};
fn main() {
    let mut file = fs::File::open("src/input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.trim().split("\n").collect();
    let mut pass_list: Vec<Password> = Vec::new();
    println!("Hello, world!");
}
