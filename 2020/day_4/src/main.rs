use std::{fs, io::Read};
use std::collections::HashMap;

fn main() {
    let mut file = fs::File::open("src/example_input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.trim().split(['\n', ' ']).collect();
    println!("{:?}", data);
}
