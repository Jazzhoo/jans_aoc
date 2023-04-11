use std::{fs, marker::Tuple};

fn check_for_cid(input: &str) -> usize {
    if input.contains("cid") {
        return 0;
    }
    else {
        return 1;
    }
}
fn validate_passport(input: &Vec<&str>) -> u32 {
    println!("{:?}", input);
    for property in input {
        let (key,val) = property.split(':', 1).collect();
    }
    1
}
fn main() {
    //reading the datafile
    let raw_data = fs::read_to_string("src/example_input").expect("error while reading file");
    let data = raw_data.split("\n\n").map(|s| s.replace("\n", " ")).collect::<Vec<String>>();
    //println!("{}", data.next().unwrap());
    let mut valid_count = 0;
    for line in &data {
        let temp_vec: Vec<&str> = line.trim().split(" ").collect();
        let temp_vec_len = temp_vec.len();
        //println!("{:?} || #: {}, val: {}", temp_vec, temp_vec_len, check_for_cid(&line));
        match temp_vec_len {
            8 => valid_count += 1,
            7 => valid_count += check_for_cid(&line),
            _ => continue,
        };
    }
    println!("==== Part 1 ====");
    println!("The # of valid passports is: {}", valid_count);
    //preparing the HashTable

    println!("==== Part 2 debug ====");
    let mut valid_count = 0;
    for line in &data {
        let temp_vec: Vec<&str> = line.trim().split(" ").collect();
        let temp_vec_len = temp_vec.len();
        //println!("{:?} || #: {}, val: {}", temp_vec, temp_vec_len, check_for_cid(&line));
        match temp_vec_len {
            8 => valid_count += validate_passport(&temp_vec),
            7 => valid_count += match check_for_cid(&line) {
                0 => 0,
                1 => validate_passport(&temp_vec),
                _ => continue,
            },
            _ => continue,
        };
    }

    println!("==== Part 2 ====");
    println!("The # of valid passports is: {}", valid_count);

}
