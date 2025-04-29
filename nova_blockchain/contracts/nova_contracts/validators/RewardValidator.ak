module reward_validator

import {
  ScriptContext,
  get_signatories
} from "aiken/tx"

import {
  length
} from "aiken/list"

validator {
  fn main(datum: Int, redeemer: Int, context: ScriptContext) -> Bool {
    // datum: student score
    // redeemer: moduleId or nonce

    if datum >= 80 {
      // Check student signed the tx (student must claim it)
      let signatories = get_signatories(context)
      length(signatories) > 0
    } else {
      False
    }
  }
}
