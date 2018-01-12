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
    pd = day |> Integer.to_string() |> String.pad_leading(2, "0")
    fname = "../day#{pd}_input.txt"
    data = File.read!(fname)
    # lines = String.split data, ~r{\r|\n|\r\n}, trim: true
    lines = String.split(data, ["\r", "\n", "\r\n"], trim: true)

    # lines = File.stream!(fname) |> Stream.map( &(String.replace(&1, "\n", "")) ) |> Enum.to_list

    case lines do
      [a] -> a
      a -> a
    end
  end

  def answer(part, correct, calculated) do
    color =
      cond do
        correct == 0 -> :yellow
        correct == calculated -> :green
        true -> :red
      end

    IO.puts(IO.ANSI.format([color, "Part #{part} Answer #{calculated}"], true))
  end
end
