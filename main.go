package main

import (
	"crypto/rand"
	"fmt"
	"math/big"

	"github.com/fatih/color"
)

func main() {
	boldCyan := color.New(color.FgCyan, color.Bold).PrintfFunc()
	boldRed := color.New(color.FgRed, color.Bold).PrintfFunc()

	n, err := rand.Int(rand.Reader, big.NewInt(10))
	if err != nil {
		fmt.Println("error")
	}

	if int(n.Int64()) >= 5 {
		boldCyan("Yes\n")
	} else {
		boldRed("No\n")
	}
}
