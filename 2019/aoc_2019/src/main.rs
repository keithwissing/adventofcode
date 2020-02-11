use std::time::Instant;
mod day01;
mod day02_hashmap;
mod day02_slice;
mod day02_vector;

fn main() {
    day01::day01();
    {
        let now = Instant::now();
        day02_hashmap::day02();
        let elapsed = now.elapsed();
        println!("HashMap : {:.2?}", elapsed);
    }
    {
        let now = Instant::now();
        day02_vector::day02();
        let elapsed = now.elapsed();
        println!("Vector : {:.2?}", elapsed);
    }
    {
        let now = Instant::now();
        day02_slice::day02();
        let elapsed = now.elapsed();
        println!("Slices : {:.2?}", elapsed);
    }
}
