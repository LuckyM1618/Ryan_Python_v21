function isPalindrome(str) {
    for(var i = 0; i < Math.ceil(str.length / 2); i++) {
        if(!(str[i] == str[str.length - i - 1])) { return false }
    }
    return true;
}

function longestPalindrome(str) {
    var start = new Date()

    for(var working_length = str.length; working_length > 0; working_length--) {
        for(var offset = 0; offset <= (str.length - working_length); offset++ ) {
            for(var i = offset; i < (offset + working_length - 1); i++) {
                var sub_str = str.substring(offset, (offset + working_length))
                if(isPalindrome(sub_str)) {
                    var end = new Date()
                    var time = end.getTime() - start.getTime();
                    console.log(time)
                    return sub_str
                }
            }
        }
    }
}


