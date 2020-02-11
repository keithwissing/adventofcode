use std::fs;

#[allow(dead_code)]
pub fn read_lines(day: i32) -> Vec<String> {
    let filename = format!("../day{:02}_input.txt", day);
    let input = fs::read_to_string(filename).expect("Could not read file");
    let values: Vec<String> = input.lines().map(|x| x.to_owned()).collect();
    values
}

pub fn read_integers(day: i32) -> Vec<i32> {
    let filename = format!("../day{:02}_input.txt", day);
    let input = fs::read_to_string(filename).expect("Could not read file");
    let values: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    values
}

pub fn read_program(day: i32) -> Vec<i32> {
    let filename = format!("../day{:02}_input.txt", day);
    let input = fs::read_to_string(filename).expect("Could not read file");
    let program: Vec<i32> = input
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    program
}

pub fn answer(day: i32, part: i32, known: i32, calculated: i32) {
    if known == calculated {
        println!(
            "Year 2019 Day {:02} part {}: {} is correct!",
            day, part, calculated
        );
    } else {
        println!(
            "Year 2019 Day {:02} part {}: {} should be {}",
            day, part, calculated, known
        );
    }
}
