use std::{fs, io::Read};

#[derive(Debug)]
struct Password {
    instruction: (u32, u32),
    letter: char, 
    pass: String,
}

fn main() {
    let mut file = fs::File::open("src/example_input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.trim().split("\n").collect();
    //let data: Vec<Vec<&str>> = data.split(" ").collect().collect();
    let mut pass_list: Vec<Password> = Vec::new();

    println!("{:?}", data);

    for line in data {
        //let temp_str: Vec<&str> = line.split(" ").collect();
        let temp_str: Vec<&str> = line.split_whitespace().collect();
        let temp_instruction: Vec<char> = temp_str[0].chars().collect();
        let (x, y) = (temp_instruction[0].to_digit(10).unwrap(),
                        temp_instruction[2].to_digit(10).unwrap());
        let temp_letter: char = temp_str[1].chars().next().unwrap();
        let temp_pass = temp_str[2];
        println!("tup: {:?}, temp_letter: {}, temp_pass: {}",
                 (x,y), temp_letter, temp_pass);
        pass_list.push(Password {
            instruction: (x, y),
            letter: temp_letter,
            pass: String::from(temp_pass),
        });
    }
        println!("{:?}", pass_list);
}
