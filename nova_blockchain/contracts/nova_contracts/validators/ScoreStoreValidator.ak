module score_store_validator

import {
  ScriptContext
} from "aiken/tx"

type StudentData = {
  hashedId: ByteArray
  score: Int
}

validator {
  fn main(datum: StudentData, _redeemer: Unit, _context: ScriptContext) -> Bool {
    // Anyone can store data, we only validate data is within score range
    datum.score >= 0 && datum.score <= 100
  }
}
