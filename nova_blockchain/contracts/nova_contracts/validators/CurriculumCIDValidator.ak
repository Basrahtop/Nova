module curriculum_cid_validator

type CurriculumDatum = {
  subject: String,
  cid: ByteArray,       // IPFS hash in bytes
  uploader: ByteArray   // PubKeyHash of admin/uploader
}

import {
  ScriptContext,
  get_signatories
} from "aiken/tx"

import {
  member
} from "aiken/list"

validator {
  fn main(datum: CurriculumDatum, _redeemer: Unit, context: ScriptContext) -> Bool {
    let signers = get_signatories(context)
    member(datum.uploader, signers)
  }
}
