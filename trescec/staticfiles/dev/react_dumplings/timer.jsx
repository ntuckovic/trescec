/*
Example usage:
==============
import Timer from 'react-dumplings/timer.jsx';

let reloadTimer = new Timer(() => {
    console.log("This timer runs every 2 seconds");
}, 2000);
*/

class Timer {

    constructor (fn, t) {
        this.fn = fn;
        this.t = t;
        this.timerObj = setInterval(this.fn, this.t);
    }

    stop () {
        if (this.timerObj) {
            clearInterval(this.timerObj);
            this.timerObj = null;
        }

        return this;
    }

    // start timer using current settings (if it's not already running)
    start () {
        if (!this.timerObj) {
            this.stop();
            this.timerObj = setInterval(this.fn, this.t);
        }

        return this;
    }

    // start with new interval, stop current interval
    reset (newT) {
        if (newT) {
            this.t = newT;
        }

        return this.stop().start();
    }
}

module.exports = Timer;
