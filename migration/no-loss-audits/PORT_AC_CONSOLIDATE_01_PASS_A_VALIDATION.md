# PORT-AC-CONSOLIDATE-01 — Pass A validation

## Control boundary

- controlling packet: `Yuren-Tang/research-workbench#87` comment `5075948677`;
- writer: `MATH-CUR::chatgpt:6a57882c-55cc-83ed-a9f8-4ce0ed7c4d8d`;
- lease generation: `20260725T005438Z-19153`;
- branch start: `curation/affine-cdc-global-rebaseline-v2@24f777d45693ff7e031dc93137a4aec5b879a7b3`;
- canonical comparison: `main@960c92b7ff231c78b387894149779083060a75eb`.

## Added additive surfaces

1. `registry/schema/mathematical-unit.schema.json`;
2. `registry/schema/typed-relation.schema.json`;
3. `sources/manifests/PORT_AC_CONSOLIDATE_01_SOURCE_MANIFEST.json`;
4. `migration/source-to-unit-map/PORT_AC_CONSOLIDATE_01_MAP.json`;
5. this validation record.

No pre-existing project path was deleted, moved, or overwritten.

## Structural validation

- both JSON schemas parse as JSON;
- the mathematical-unit schema separates form, maturity, assurance evidence, disposition, workflow, provenance, relations, and views;
- the relation schema separates logical relations from discovery relations and prevents discovery types from occupying the logical plane;
- all six immutable source refs occur exactly once in the source manifest and exactly once in the migration skeleton;
- all six SHAs have forty lowercase hexadecimal characters;
- manifest counts are `6 total / 0 itemized / 6 pending`;
- migration counts are `6 source packets total / 0 classified / 6 unclassified`;
- all new observations default to `captured/unreviewed`;
- no curation action is allowed to upgrade theorem assurance.

## Pass-A checkpoint meaning

This checkpoint establishes only the registry contract and a visible six-packet backlog. It does not classify any source theorem, accept mathematics, alter the existing AffineCDC corpus, or move `main`.

Pass B must replace each packet-level `unclassified` entry with an exhaustive item-level source-to-unit classification. The required final invariant remains:

`unclassified = 0`.
