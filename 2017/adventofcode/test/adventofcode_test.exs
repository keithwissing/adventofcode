defmodule AdventofcodeTest do
  use ExUnit.Case
  doctest Adventofcode
  doctest Day01
  doctest Day02
  doctest Day04

  test "greets the world" do
    assert Adventofcode.hello() == :world
  end
end
