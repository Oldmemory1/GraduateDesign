actions_list=[
    "create_fake_signature",
    "insert_useless_data_to_end",
    "modify_checksum",
    "modify_timestamp",
    "rename_random_section",
    # but if we execute this action, other action can not be executed because they will break signature
    "upx_encryption",
    # the encryption can only be executed once
    "action_add_benign_data_overlay_1",
    "action_add_bytes_to_section_cave_1"
]