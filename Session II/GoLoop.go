package main 
import "fmt"
import "time"

func main(){
	var val int
	t1:= time.Now()
	for i:=0; i<100000000; i++{
		val = val+i
	}
	t2:= time.Now()
	diff:= t2.Sub(t1)
	fmt.Println(diff)
}