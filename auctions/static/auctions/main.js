console.log('Hello World')

const auctionBox = document.getElementById('auction-box')
const countdownBox = document.getElementById('countdown-box')

console.log(auctionBox.textContent)
const auctionDate = Date.parse(auctionBox.textContent)
console.log(auctionDate)

const myAuctionCountdown = setInterval(() => {
    const now = new Date().getTime()
    // console.log(now)

    const difference = auctionDate - now
    // console.log(difference)

    const days_left = Math.floor(auctionDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
    console.log(days_left)
    const hours_left = Math.floor((auctionDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
    console.log(hours_left)
    const minutes_left = Math.floor((auctionDate / (1000 * 60) - (now / (1000 * 60))) % 60)
    console.log(minutes_left)
    const seconds_left = Math.floor((auctionDate / (1000) - (now / (1000))) % 60)
    console.log(seconds_left)

    if (difference > 0) {
        countdownBox.innerHTML = days_left + "days," + hours_left + "hours," + minutes_left + "minutes," + seconds_left + "seconds"
    } else {
        clearInterval(myAuctionCountdown)
        countdownBox.innerHTML = "Auction countdown completed"
    }
}, 1000)

