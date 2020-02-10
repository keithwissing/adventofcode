use std::fs;

fn fuel(x: &i32) -> i32 {
    let ret = x / 3 - 2;
    ret
}

fn plus_fuel(x: &i32) -> i32 {
    let mut total = fuel(x);
    let mut more = fuel(&total);
    while more > 0 {
        total = total + more;
        more = fuel(&more);
    }
    total
}

pub fn day01() {
    let filename = "../day01_input.txt";
    let input = fs::read_to_string(filename).expect("Could not read file");
    let values: Vec<i32> = input.lines().map(|x| x.parse::<i32>().unwrap()).collect();
    let part1: i32 = values.iter().map(fuel).sum();
    println!("Day 01 Part 1 answer: {}", part1);
    let part2: i32 = values.iter().map(plus_fuel).sum();
    println!("Day 01 Part 2 answer: {}", part2);
}
