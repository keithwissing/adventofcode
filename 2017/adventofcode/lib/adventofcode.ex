defmodule Adventofcode do
  @moduledoc """
  Documentation for Adventofcode.
  """

  @doc """
  Hello world.

  ## Examples

      iex> Adventofcode.hello
      :world

  """
  def hello do
    :world
  end

  @doc """
  """
  def read_input(day) do
    pd = day |> Integer.to_string |> String.pad_leading(2, "0")
    data = File.read! "../day#{pd}_input.txt"
    lines = String.split data, "\n", trim: true
    case lines do
      [a] -> a
      a -> a
    end
  end

  def answer(part, correct, calculated) do
    IO.puts "Part #{part} Answer #{calculated}"
  end
end
