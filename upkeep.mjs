import axios from 'axios';

const URL = "https://www.backend.tedxpvgcoet.in/";
let failCount = 0;

async function checkBackendStatus() {
  try {
    const start = Date.now();
    const res = await axios.get(URL, { timeout: 40000 });
    const end = Date.now();

    console.log("✅ Backend responded:", res.data || "OK");
    console.log(`⏱️ Response time: ${(end - start) / 1000}s`);

    failCount = 0;
  } catch (err) {
    failCount++;
    console.error(`❌ Attempt ${failCount}: ${err.message}`);

    if (failCount <= 3) {
      await new Promise(r => setTimeout(r, 2000));
      return checkBackendStatus();
    } else {
      console.error("🚨 Backend unreachable after 3 retries.");
      process.exit(1);
    }
  }
}

const startTime = Date.now();
const duration = 5.5 * 3600 * 1000;

while (Date.now() - startTime < duration) {
  await checkBackendStatus();
  const istNow = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
  console.log("☝️ Ping at", istNow);
  console.log("--------------------------");
  await new Promise(resolve => setTimeout(resolve, 5 * 60 * 1000));
}
