use std::{fs};


fn main() {
    let raw_data = fs::read_to_string("src/example_input").expect("error while reading file");
    let raw_data = raw_data.trim().split("\n").collect::<Vec<&str>>();
    println!("{:?}", raw_data);


    for pass in &raw_data {
        println!("{}", pass);
    }
}
