module certificate_nft_policy

import {
  ScriptContext,
  TxOutput,
  get_mint,
  AssetName,
  TokenName,
  Value,
  PubKeyHash,
  script_hash,
} from "aiken/tx"

validator {
  fn main(course_id: TokenName, student_pkh: PubKeyHash, context: ScriptContext) -> Bool {
    let minted = get_mint(context)
    let this_policy = script_hash()

    let expected_token = {
      policy_id: this_policy,
      token_name: course_id,
      amount: 1
    }

    // Check NFT with the correct name was minted exactly once under this policy
    minted == [expected_token]
  }
}
