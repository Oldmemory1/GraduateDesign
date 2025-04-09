actions_list=[
    "action_create_fake_signature",
    "action_insert_useless_data_to_end",
    "action_modify_checksum",
    "action_modify_timestamp",
    "action_rename_random_section",
    # but if we execute this action, other action can not be executed because they will break signature
    "upx_encryption",
    # the encryption can only be executed once
    "action_add_benign_data_overlay_1",
    "action_add_bytes_to_section_cave_1",
    "action_add_section_benign_data_1",
    "action_break_optional_header_checksum_1",
    "action_modify_optional_header_1",
    "action_modify_timestamp_1",
    "action_remove_debug",
]