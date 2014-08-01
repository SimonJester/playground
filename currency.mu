contract.storage[tx.origin()] = 10**20

return compile {
    var to = this.data[0]
    var from = tx.origin()
    var value = this.data[1]

    if contract.storage[from] > value {
        contract.storage[from] = contract.storage[from] - value
        contract.storage[to] = contract.storage[to] + value
    }
}
