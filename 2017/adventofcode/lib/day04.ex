defmodule Day04 do
  import Adventofcode

  @moduledoc """
  Documentation for Day04.
  """

  @doc """
  iex> Day04.isvalid1("aa bb cc dd ee")
  true
  iex> Day04.isvalid1("aa bb cc dd aa")
  false
  iex> Day04.isvalid1("aa bb cc dd aaa")
  true
  """
  def isvalid1(passphrase) do
    pre = passphrase |> String.split()
    post = pre |> Enum.sort() |> Enum.dedup()
    length(pre) == length(post)
  end

  def part1(phrases) do
    phrases |> Enum.count(&isvalid1/1)
  end

  @doc """
  iex> Day04.isvalid2("abcde fghij")
  true
  iex> Day04.isvalid2("abcde xyz ecdab")
  false
  iex> Day04.isvalid2("a ab abc abd abf abj")
  true
  iex> Day04.isvalid2("iiii oiii ooii oooi oooo")
  true
  iex> Day04.isvalid2("oiii ioii iioi iiio")
  false
  """
  def isvalid2(passphrase) do
    pre =
      passphrase
      |> String.split()
      |> Enum.map(fn x -> String.graphemes(x) |> Enum.sort() |> Enum.join() end)

    post = pre |> Enum.sort() |> Enum.dedup()
    length(pre) == length(post)
  end

  def part2(phrases) do
    phrases |> Enum.count(&isvalid2/1)
  end

  def run do
    input = read_input(4)
    answer(1, 451, part1(input))
    answer(2, 223, part2(input))
  end
end
