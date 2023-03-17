use std::{fs, io::Read};
use std::collections::HashMap;

fn check_for_cid(input: &str) -> usize {
    if input.contains("cid") {
        return 0;
    }
    else {
        return 1;
    }
}

fn main() {
    //reading the datafile
    let raw_data = fs::read_to_string("src/input").expect("error while reading file");
    let data = raw_data.split("\n\n").map(|s| s.replace("\n", " "));
    //println!("{}", data.next().unwrap());
    let mut valid_count = 0;
    for line in data {
        let temp_vec: Vec<&str> = line.trim().split(" ").collect();
        let temp_vec_len = temp_vec.len();
        println!("{:?} || #: {}, val: {}", temp_vec, temp_vec_len, check_for_cid(&line));
        match temp_vec_len {
            8 => valid_count += 1,
            7 => valid_count += check_for_cid(&line),
            _ => continue,
        };
    }
    println!("The # of valid passports is: {}", valid_count);
    //preparing the HashTable
    
    


}
