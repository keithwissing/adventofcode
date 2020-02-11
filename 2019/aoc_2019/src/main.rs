use std::time::Instant;
mod day01;
mod day02_hm;
mod day02_s;
mod day02_v;

fn main() {
    day01::day01();
    {
        let now = Instant::now();
        day02_hm::day02();
        let elapsed = now.elapsed();
        println!("HashMap : {:.2?}", elapsed);
    }
    {
        let now = Instant::now();
        day02_v::day02();
        let elapsed = now.elapsed();
        println!("Vector : {:.2?}", elapsed);
    }
    {
        let now = Instant::now();
        day02_s::day02();
        let elapsed = now.elapsed();
        println!("Slices : {:.2?}", elapsed);
    }
}
