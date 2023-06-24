use std::fs;
use std::collections::{HashSet, HashMap, VecDeque};

fn main() {
    let raw_data = fs::read_to_string("src/example_input")
        .expect("Something wrong with file read");
    println!("{:?}", raw_data);
}
