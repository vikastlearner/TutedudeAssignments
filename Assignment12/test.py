(
    dhcpoption_type &&
    dhcpoption_name &&
    (
        (dhcp_id || dhcp_name)

        ||

        (
            dhcpscope_id ||
            (
                scope_name &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )

        ||

        (
            dhcpacl_id ||
            (
                acl_name &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )

        ||

        (
            dhcpacl_data_id ||
            (
                acl_data_value &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )

        ||

        (
            dhcpgroup_id ||
            (
                group_name &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )

        ||

        (
            dhcprange_id ||
            (
                range_name &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )

        ||

        (
            dhcphost_id ||
            (
                host_name &&
                (dhcp_id || dhcp_name || hostaddr)
            )
        )
    )
)