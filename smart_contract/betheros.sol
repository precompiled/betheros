//Betheros - transparent and reliable platform for bettering open source projects.

pragma solidity ^0.4.13;
/// @title Betheros
/// @author karike

contract Betheros {
    uint constant ACTUAL_DONATION_PERCENTAGE = 99;
    uint constant BASELINE_REWARD = 30 szabo;//== 0.00003 ETH
    uint constant MAX_CONTRIBUTION_COEFFICIENT = 100000;//== max 3 ETH
    uint constant MAX_NUMBER_LINES = 2000;
    uint constant MIN_NUMBER_LINES = 50;
    uint[] public actionPoints;

    address administrator;//language provides to check administrator.balance ?
    uint public totalBalance;
    mapping (string => address) contributors;//KISS
    mapping (string => uint) contributorCoefficients;

    modifier onlyOwner {
        require(msg.sender == administrator);
        _;
    }

    event DonationReceived(string donatorName, uint amount);
    event ContributorAdded(string username, address addr);
    event ContributorRewarded(string username, uint amount, uint action);

    function Betheros()  payable {
        administrator = msg.sender;
        totalBalance += msg.value;//add some initial investment

        actionPoints.push(3000);//0-PullRequestDeveloper
        actionPoints.push(1000);//1-PullRequestReviewer
        actionPoints.push(500);//2-IssueSolved
        actionPoints.push(5000);//3-FutureFeatureEnhancement

        addContributor("dontstop", 0xaf2aa3E0226856aE1e0E92021f5F6D5F552437b2);
    }

    function donate(string donatorName) payable {
        //1% of the donation is needed to keep the system running
        uint actualDonation = (msg.value * ACTUAL_DONATION_PERCENTAGE) / 100;
        administrator.transfer(msg.value - actualDonation);

        totalBalance += actualDonation;

        DonationReceived(donatorName, actualDonation);
    }

    function getContribution(string username) returns (uint) {
        return contributorCoefficients[username];
    }

    function handleContribution(string username, uint action, uint numberLines) onlyOwner {
        require(contributors[username] > 0);
        require(action < actionPoints.length);
        uint numberLinesReward = numberLines;
        if (action < 2) {
        if (numberLines > MAX_NUMBER_LINES) {
            numberLinesReward = MAX_NUMBER_LINES;
        }
        if (numberLines < MIN_NUMBER_LINES) {
            numberLinesReward = MIN_NUMBER_LINES;
        }
        }
        if (contributorCoefficients[username] + actionPoints[action] + numberLinesReward > MAX_CONTRIBUTION_COEFFICIENT) {
            contributorCoefficients[username] = MAX_CONTRIBUTION_COEFFICIENT;
        }
        else {
            contributorCoefficients[username] = contributorCoefficients[username] + actionPoints[action] + numberLinesReward;
        }

        uint amount = BASELINE_REWARD * contributorCoefficients[username];
        contributors[username].transfer(amount);

        ContributorRewarded(username, amount, action);
    }

    function addContributor(string username, address addr) onlyOwner{
        contributors[username] = addr;

        ContributorAdded(username, addr);
    }

    function addAction(uint actionCoefficient) onlyOwner {
        actionPoints.push(actionCoefficient);
    }
}