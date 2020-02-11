use std::time::Instant;
mod aoc;
mod day01;
mod day02_hashmap;
mod day02_slice;
mod day02_vector;

fn run_day2(label: &str, program: &[i32], func: fn(&[i32]) -> (i32, i32)) {
    let now = Instant::now();
    let (p1, p2) = func(&program);
    let elapsed = now.elapsed();
    aoc::answer(2, 1, 5305097, p1);
    aoc::answer(2, 2, 4925, p2);
    println!("{} : {:.2?}", label, elapsed);
}

fn run_day<T>(day: i32, a1: i32, a2: i32, i: &T, func: fn(&T) -> (i32, i32)) {
    let now = Instant::now();
    let (p1, p2) = func(i);
    let elapsed = now.elapsed();
    aoc::answer(day, 1, a1, p1);
    aoc::answer(day, 2, a2, p2);
    println!("Day {:02} : {:.2?}", day, elapsed);
}

fn main() {
    run_day(1, 3219099, 4825810, &aoc::read_integers(1), |i| {
        day01::day01(i)
    });

    let program = aoc::read_program(2);
    run_day2("HashMap", &program, |p| day02_hashmap::day02(p));
    run_day2("Vector", &program, |p| day02_vector::day02(p));
    run_day2("Slice", &program, |p| day02_slice::day02(p));
}
