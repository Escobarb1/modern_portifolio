let day = "nesday";

switch (day) {
    case 'Monday':
        console.log("7am 📢🔊");
        break;
    case 'Tuesday':
    case 'Wednesday':
    case 'Thursday':
        console.log("4am 📢🔊");
        break;
    case 'Friday':
        console.log("9am 📢🔊");
        break;
    case 'Saturday':
    case 'Sunday':
        console.log("8am 📢🔊");
        break;
    default:
        console.log("7am - Watching videos 😆😆");
}