// SPDX-License-Identifier: AGPL-3.0-only
pragma solidity ^0.8.0;

import "./ERC20.sol";

contract ModernToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("ModernToken", "MTK", 18) {
        _mint(msg.sender, initialSupply);
    }
}
