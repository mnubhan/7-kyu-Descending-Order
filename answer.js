const descendingOrder = num =>{
    return parseInt(num.toString().split("").sort((x,y)=>y-x).join(""))
}
