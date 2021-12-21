import Foundation

func solution(_ nTuple:String) -> [Int] {
    var nTupleComponents = nTuple.components(separatedBy: "},{")
    let firstTuple = String(nTupleComponents[0].dropFirst().dropFirst())
    nTupleComponents[0] = firstTuple
    let lastTuple = String(nTupleComponents[nTupleComponents.count - 1].dropLast().dropLast())
    nTupleComponents[nTupleComponents.count - 1] = lastTuple

    let orderedTupleSet = nTupleComponents
        .map { $0.components(separatedBy: ",") }
        .sorted(by: { $0.count < $1.count })
    var counter = [String: Int]()
    orderedTupleSet.forEach {
        $0.forEach {
            if let countOfTupleElement = counter[$0] {
                counter[$0] = countOfTupleElement + 1
            } else {
                counter[$0] = 1
            }
        }
    }
    return counter.sorted { $0.value > $1.value } .map({$0.key}).compactMap({ Int($0) })
}
