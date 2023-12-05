# Powershell scripts that make my life easier

# Set the AOC directory and cookie
$env:AOC = "{path}\Advent-of-Code" # Change this to your AOC directory
$env:AOC_COOKIE = "..." #Change this to your own session cookie

# Used to get the day's input
function get-aoc {
    param(
        [int]$day
    )
    Invoke-WebRequest -Uri "https://adventofcode.com/2023/day/$day/input" -Headers @{ "cookie" = "session=$env:AOC_COOKIE" } -OutFile in.txt
}

# Create the new day's files and folders
function new-day {
    param(
        [int]$number
    )

    $folderName = "Day $number"
    $part1Folder = "$folderName\Part 1"
    $part2Folder = "$folderName\Part 2"

    Set-Location $env:AOC

    # Create directories
    $directories = $folderName, $part1Folder, $part2Folder
    foreach ($dir in $directories) {
        New-Item -ItemType Directory -Path $dir -ErrorAction SilentlyContinue | Out-Null
    }

    # Create solution files
    $solutionFiles = "$part1Folder\solution.go", "$part1Folder\solution.py", "$part2Folder\solution.py", "$part2Folder\solution.go"
    foreach ($file in $solutionFiles) {
        New-Item -Path $file -ErrorAction SilentlyContinue | Out-Null
    }

    Set-Location -Path $part1Folder
    get-aoc -day $number
    Set-Location -Path $part2Folder
    get-aoc -day $number

    Set-Location $env:AOC
}

# Used to run the python solutions
function out-aocp {
    param(
        [int]$day,
        [int]$part
    )

    $dayFolder = "Day $day"
    $partFolder = "Part $part"

    Set-Location "$env:AOC\$dayFolder\$partFolder"
    python.exe solution.py
    Set-Location $env:AOC
}