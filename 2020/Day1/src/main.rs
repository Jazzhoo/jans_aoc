use std::fs;

fn main() {
    let content = fs::read_to_string("src/example_input")
        .expect("file not found");
    println!("The input is: \n{content}");
}
