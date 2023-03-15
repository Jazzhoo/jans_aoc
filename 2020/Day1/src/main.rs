use std::{fs, io::Read};
fn main() {
    let mut file = fs::File::open("src/input")
        .expect("file not found");
    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("error while reading file");

    let data: Vec<&str> = data.split("\n").collect();
    let data: Vec<u32> = data.iter().map(|x| x.parse().unwrap()).collect();
    let mut result: u32;
    //println!("{:?}", data);
    println!("==Part 1==");

    'outer_loop: for x in &data {
        for y in &data {
            //println!("x: {x}, y: {y}");
            if x == y {
                continue;
            }
            else if x + y == 2020 {
                result = y * x;
                println!("the numbers are x: {x} y: {y}");
                println!("the solution is {result}");
                break 'outer_loop;
            }
        }
    }
    println!("==Part 2==");
    'outer_loop: for x in &data {
        for y in &data {
            //println!("x: {x}, y: {y}");
            if x == y {
                continue;
            }
            for z in &data {
                if z == x || z == y {
                    continue;
                }
                else if x + y + z == 2020 {
                    result = y * x * z;
                    println!("the numbers are x: {x} y: {y} z: {z}");
                    println!("the solution is {result}");
                    break 'outer_loop;

                }
            }
        }
    }



}
